using System;
using System.IO;
using Microsoft.Kinect;

namespace KinectSkeletonRecording
{
    class Program
    {
        static KinectSensor sensor;
        static StreamWriter fileWriter;

        static void Main(string[] args)
        {
            // Initialize Kinect Sensor
            sensor = KinectSensor.KinectSensors[0];
            sensor.SkeletonStream.Enable();
            sensor.SkeletonFrameReady += Sensor_SkeletonFrameReady;

            // Start the sensor
            sensor.Start();

            // Create a file to record the skeleton data
            fileWriter = new StreamWriter("SkeletonData.txt");

            Console.WriteLine("Recording skeleton data. Press any key to stop...");
            Console.ReadKey();

            // Stop the sensor
            sensor.Stop();
            fileWriter.Close();
        }

        static void Sensor_SkeletonFrameReady(object sender, SkeletonFrameReadyEventArgs e)
        {
            using (SkeletonFrame skeletonFrame = e.OpenSkeletonFrame())
            {
                if (skeletonFrame != null)
                {
                    Skeleton[] skeletons = new Skeleton[skeletonFrame.SkeletonArrayLength];
                    skeletonFrame.CopySkeletonDataTo(skeletons);

                    foreach (Skeleton skel in skeletons)
                    {
                        if (skel.TrackingState == SkeletonTrackingState.Tracked)
                        {
                            // Record the skeleton data
                            // Test data: Timestamp, trackingID, positionX, positionY, positionZ
                            fileWriter.WriteLine($"{DateTime.Now}, {skel.TrackingId}, {skel.Position.X}, {skel.Position.Y}, {skel.Position.Z}");
                        }
                    }
                }
            }
        }
    }
}
