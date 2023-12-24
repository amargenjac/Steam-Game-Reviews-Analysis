package org.example;

import java.io.IOException;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.FloatWritable;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class GameCount {

    public static class TokenizerMapper
            extends Mapper<Object, Text, Text, IntWritable>{

        private final static IntWritable one = new IntWritable(1);

        public void map(Object key, Text value, Context context
        ) throws IOException, InterruptedException {
            String row = value.toString();
            String[] splitted = row.split(",");

            // Check if the row has the "recommended" field
            if (splitted.length >= 4) {
                String name = splitted[2].trim();
                String recommended = splitted[3].trim();

                // Emit the unique name and "recommended" value as the key
                context.write(new Text(name + "," + recommended), one);
            }
        }
    }

    public static class FloatSumReducer
            extends Reducer<Text,IntWritable,Text,FloatWritable> {
        private FloatWritable result = new FloatWritable();

        public void reduce(Text key, Iterable<IntWritable> values,
                           Context context
        ) throws IOException, InterruptedException {
            int totalCount = 0;
            int trueCount = 0;

            // Count the total occurrences and the occurrences where "recommended" is true
            for (IntWritable val : values) {
                totalCount += val.get();
                if (key.toString().endsWith(",true")) {
                    trueCount += val.get();
                }
            }

            // Calculate the percentage
            float percentage = (float) trueCount / totalCount * 100.0f;

            result.set(percentage);
            context.write(key, result);
        }
    }

    public static void main(String[] args) throws Exception {
        Configuration conf = new Configuration();
        Job job = Job.getInstance(conf, "game percentage");
        job.setJarByClass(GameCount.class);
        job.setMapperClass(TokenizerMapper.class);
        job.setCombinerClass(FloatSumReducer.class);
        job.setReducerClass(FloatSumReducer.class);
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(FloatWritable.class);
        FileInputFormat.addInputPath(job, new Path(args[0]));
        FileOutputFormat.setOutputPath(job, new Path(args[1]));
        System.exit(job.waitForCompletion(true) ? 0 : 1);
    }
}
