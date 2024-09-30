import * as React from "react";
import { Card } from "@/components/ui/card";
import { useSelector } from "react-redux";
import { RootState } from "@/redux/store";
import WorkoutMap from "./components/analytics/WorkoutMap";
import WorkoutCharts from "./components/analytics/WorkoutCharts";

interface Props {}

const WorkoutMetricsDisplay: React.FC<Props> = (props: Props) => {
  const selectedWorkout = useSelector(
    (state: RootState) => state.selectedWorkout.workout
  );

  return (
    <Card className="w-full h-full">
      <WorkoutMap
        lat={selectedWorkout?.workoutRoute.latitude ?? []}
        long={selectedWorkout?.workoutRoute.longitude ?? []}
      />
      <WorkoutCharts workout={selectedWorkout} />
    </Card>
  );
};

export default WorkoutMetricsDisplay;
