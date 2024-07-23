using System;
using System.IO;
using Microsoft.Kinect;

namespace KinectSkeletonRecording
{
    class Recorder
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

            // Create a CSV file to record the skeleton data
            fileWriter = new StreamWriter("SkeletonData.csv");

            // Write CSV header
            fileWriter.WriteLine("Timestamp,TrackingID," + 
                "SpineBaseX,SpineBaseY,SpineBaseZ," +
                "SpineMidX,SpineMidY,SpineMidZ," +
                "NeckX,NeckY,NeckZ," +
                "HeadX,HeadY,HeadZ," +
                "ShoulderLeftX,ShoulderLeftY,ShoulderLeftZ," +
                "ElbowLeftX,ElbowLeftY,ElbowLeftZ," +
                "WristLeftX,WristLeftY,WristLeftZ," +
                "HandLeftX,HandLeftY,HandLeftZ," +
                "ShoulderRightX,ShoulderRightY,ShoulderRightZ," +
                "ElbowRightX,ElbowRightY,ElbowRightZ," +
                "WristRightX,WristRightY,WristRightZ," +
                "HandRightX,HandRightY,HandRightZ," +
                "HipLeftX,HipLeftY,HipLeftZ," +
                "KneeLeftX,KneeLeftY,KneeLeftZ," +
                "AnkleLeftX,AnkleLeftY,AnkleLeftZ," +
                "FootRightX,FootRightY,FootRightZ," +
                "SpineShoulderX,SpineShoulderY,SpineShoulderZ," +
                "HandTipLeftX,HandTipLeftY,HandTipLeftZ," +
                "ThumbLeftX,ThumbLeftY,ThumbLeftZ," +
                "HandTipRightX,HandTipRightY,HandTipRightZ," +
                "ThumbRightX,ThumbRightY,ThumbRightZ");

// # SpineBase: 0
// # SpineMid: 1
// # Neck: 2
// # Head: 3
// # ShoulderLeft: 4
// # ElbowLeft: 5
// # WristLeft: 6
// # HandLeft: 7
// # ShoulderRight: 8
// # ElbowRight: 9
// # WristRight: 10
// # HandRight: 11
// # HipLeft: 12
// # KneeLeft: 13
// # AnkleLeft: 14
// # FootLeft: 15
// # HipRight: 16
// # KneeRight: 17
// # AnkleRight: 18
// # FootRight: 19
// # SpineShoulder: 20
// # HandTipLeft: 21
// # ThumbLeft: 22
// # HandTipRight: 23
// # ThumbRight: 24


            Console.WriteLine("Recording skeleton data to CSV. Press any key to stop...");
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
                            fileWriter.Write($"{DateTime.Now},{skel.TrackingId},");

                            // Record the position of each joint
                            foreach (Joint joint in skel.Joints)
                            {
                                fileWriter.Write($"{joint.Position.X},{joint.Position.Y},{joint.Position.Z},");
                            }

                            // Remove the trailing comma and add a newline
                            fileWriter.WriteLine();
                        }
                    }
                }
            }
        }
    }
}
