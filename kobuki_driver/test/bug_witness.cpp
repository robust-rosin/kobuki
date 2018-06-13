#include "kobuki_driver/modules/diff_drive.hpp"
#include <ros/ros.h>
#include <gtest/gtest.h>

TEST(TestSuite, bugWitness)
{
  const double cmd_speed = 10.0;
  const double cmd_radius = 0.0;
  kobuki::DiffDrive drive;
  drive.velocityCommands(cmd_speed, cmd_radius);
  std::vector<short> commands = drive.velocityCommands();
  EXPECT_EQ((short) 10000, commands[0]);
}

int main(int argc, char **argv){
  testing::InitGoogleTest(&argc, argv);
  ros::init(argc, argv, "tester");
  ros::NodeHandle nh;
  return RUN_ALL_TESTS();
}
