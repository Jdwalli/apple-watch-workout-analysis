import React from "react";
import { CardContent } from "@/components/ui/card";
import { useSelector } from "react-redux";
import { RootState } from "@/redux/store";
import WorkoutMetricsTabs from "./WorkoutMetricsTabs";
import WorkoutMetricsHeader from "./metrics/WorkoutMetricsHeader";
import WorkoutMetricsDefaultCards from "./metrics/WorkoutMetricsDefaultCards";

const WorkoutMetadataOutput: React.FC = () => {
  const selectedWorkout = useSelector(
    (state: RootState) => state.selectedWorkout.workout
  );

  React.useEffect(() => {}, [selectedWorkout]);

  return (
    <CardContent className="h-full">
      {selectedWorkout ? (
        <>
          <WorkoutMetricsHeader workout={selectedWorkout} />
          <WorkoutMetricsDefaultCards workout={selectedWorkout} />
          <WorkoutMetricsTabs workout={selectedWorkout} />
        </>
      ) : (
        <p> No content loaded yet </p>
      )}
    </CardContent>
  );
};

export default WorkoutMetadataOutput;
