import React from "react";
import { CardContent } from "@/components/ui/card";
import { useSelector } from "react-redux";
import { RootState } from "@/redux/store";
import WorkoutMetricsTabs from "./WorkoutMetricsTabs";
import WorkoutMetricsHeader from "./metrics/WorkoutMetricsHeader";
import WorkoutMetricsDefaultCards from "./metrics/WorkoutMetricsDefaultCards";
import { Skeleton } from "@/components/ui/skeleton";

const WorkoutMetadataOutput: React.FC = () => {
  const selectedWorkout = useSelector(
    (state: RootState) => state.selectedWorkout.workout
  );

  const workoutLoadingStatus = useSelector(
    (state: RootState) => state.workoutLoadingStatus.workoutLoadingStatus
  );

  React.useEffect(() => {}, [selectedWorkout]);

  return (
    <CardContent className="h-full">
      {workoutLoadingStatus ? (
        <>
          <Skeleton className="mt-10 h-10 w-full mb-4" />
          <Skeleton className="h-24 w-full mb-4" />
          <Skeleton className="h-full w-full mb-4" />
        </>
      ) : selectedWorkout ? (
        <>
          <WorkoutMetricsHeader workout={selectedWorkout} />
          <WorkoutMetricsDefaultCards workout={selectedWorkout} />
          <WorkoutMetricsTabs workout={selectedWorkout} />
        </>
      ) : (
        <div className="p-4 w-full flex justify-center">
          <p className="text-2xl">{`Please select a date`}</p>
        </div>
      )}
    </CardContent>
  );
};

export default WorkoutMetadataOutput;
