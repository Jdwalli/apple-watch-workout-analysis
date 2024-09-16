import React from "react";
import { useSelector } from "react-redux";
import { RootState } from "../../redux/store";
import { WorkoutContext } from "@/types/client_types";

import WorkoutControlPanel from "./WorkoutControlPanel";
import WorkoutMetricsDisplay from "./WorkoutMetricsDisplay";

const WorkoutsPage: React.FC = () => {
  const [workoutContext, setWorkoutContext] = React.useState<WorkoutContext>();

  const selectedWorkoutDate = useSelector(
    (state: RootState) => state.selectedWorkoutDate
  );

  return (
    <div className="container relative h-full flex-col items-center justify-center grid lg:max-w-none grid-cols-[35%,65%] px-0">
      <WorkoutControlPanel />
      <WorkoutMetricsDisplay />
    </div>
  );
};

export default WorkoutsPage;
