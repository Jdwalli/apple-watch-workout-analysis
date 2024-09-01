import React from "react";
import { WorkoutApiClient } from "../clients/workout_client";

interface Props {}

const WorkoutsPage: React.FC<Props> = (props: Props) => {
  const workoutClient = new WorkoutApiClient()

  return (
    <div className="">
      <h1> Workouts Page</h1>
    </div>
  );
};

export default WorkoutsPage;