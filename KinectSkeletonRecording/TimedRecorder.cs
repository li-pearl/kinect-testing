using System;
using System.IO;
using System.Timers;
using Microsoft.Kinect;

namespace KinectSkeletonRecording
{
    class Recorder
    {
        static KinectSensor sensor;
        static StreamWriter fileWriter;
        static Timer timer;
        static bool recording = false;

        static void Main(string[] args)
        {
            // Prompt for CSV file name
            Console.Write("Enter the name of the CSV file: ");
            string csvFileName = Console.ReadLine() + ".csv";

            // Prompt for recording duration in seconds
            Console.Write("Enter the recording duration in seconds: ");
            double recordingDurationSeconds = Convert.ToDouble(Console.ReadLine());
            double recordingDurationMilliseconds = SecondsToMilliseconds(recordingDurationSeconds);

            // Ask if the user wants to start recording
            Console.Write("Do you want to start recording? (y/n): ");
            string startRecording = Console.ReadLine().ToLower();

            while (startRecording != "y" && startRecording != "n")
            {
                Console.Write("Invalid input. Please enter 'y' to start recording or 'n' to exit: ");
                startRecording = Console.ReadLine().ToLower();
            }

            if (startRecording == "n")
            {
                Console.WriteLine("Program ended.");
                return;
            }

            if (startRecording == "y")
            {
                Console.WriteLine($"Recording duration: {recordingDurationSeconds} seconds.");
                Console.WriteLine("Recording skeleton data to CSV...");

                // Initialize Kinect Sensor
                sensor = KinectSensor.KinectSensors[0];
                sensor.SkeletonStream.Enable();
                sensor.SkeletonFrameReady += Sensor_SkeletonFrameReady;

                // Start the sensor
                sensor.Start();

                // Create a CSV file to record the skeleton data
                fileWriter = new StreamWriter(csvFileName);

                // Write CSV header. The order matters for visualization and data processing!
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
                    "FootLeftX,FootLeftY,FootLeftZ," +
                    "HipRightX,HipRightY,HipRightZ," +
                    "KneeRightX,KneeRightY,KneeRightZ," +
                    "AnkleRightX,AnkleRightY,AnkleRightZ," +
                    "FootRightX,FootRightY,FootRightZ," +
                    "SpineShoulderX,SpineShoulderY,SpineShoulderZ," +
                    "HandTipLeftX,HandTipLeftY,HandTipLeftZ," +
                    "ThumbLeftX,ThumbLeftY,ThumbLeftZ," +
                    "HandTipRightX,HandTipRightY,HandTipRightZ," +
                    "ThumbRightX,ThumbRightY,ThumbRightZ,");

                // Set up the timer
                timer = new Timer(recordingDurationMilliseconds);
                timer.Elapsed += TimerElapsed;
                timer.AutoReset = false;
                timer.Start();

                // Set recording flag
                recording = true;

                Console.WriteLine("Recording started. Press any key to stop manually...");
                Console.ReadKey();

                // Stop the sensor if still recording
                if (recording)
                {
                    StopRecording();
                }

                // Ensure the program exits after stopping
                Environment.Exit(0);
            }
            else
            {
                Console.WriteLine("Program ended.");
            }
        }

        static void Sensor_SkeletonFrameReady(object sender, SkeletonFrameReadyEventArgs e)
        {
            if (!recording) return;

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

        static void TimerElapsed(object sender, ElapsedEventArgs e)
        {
            StopRecording();
        }

        static void StopRecording()
        {
            if (recording)
            {
                recording = false;
                sensor.Stop();
                fileWriter.Close();
                Console.WriteLine("Recording stopped. Data saved to CSV file.");
                return;
            }
        }

        static double SecondsToMilliseconds(double seconds)
        {
            return seconds * 1000;
        }
    }
}
