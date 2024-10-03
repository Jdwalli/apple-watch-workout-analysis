import React from "react";
import { Card } from "@/components/ui/card";
import { useSelector } from "react-redux";
import { RootState } from "@/redux/store";
import WorkoutMap from "./components/analytics/WorkoutMap";
import WorkoutCharts from "./components/analytics/WorkoutCharts";
import { Skeleton } from "@/components/ui/skeleton";

const WorkoutMetricsDisplay: React.FC = () => {
  const selectedWorkout = useSelector(
    (state: RootState) => state.selectedWorkout.workout
  );

  const workoutLoadingStatus = useSelector(
    (state: RootState) => state.workoutLoadingStatus.workoutLoadingStatus
  );

  return (
    <Card className="w-full h-full overflow-hidden">
      {workoutLoadingStatus ? (
        <WorkoutMap lat={[]} long={[]} />
      ) : (
        <WorkoutMap
          lat={selectedWorkout?.workoutRoute.latitude ?? []}
          long={selectedWorkout?.workoutRoute.longitude ?? []}
        />
      )}

      {workoutLoadingStatus ? (
        <>
          <Skeleton className="h-24 mt-2 w-full mb-4" />
          <Skeleton className="h-full w-full mb-4" />
        </>
      ) : selectedWorkout ? (
        <>
          <WorkoutCharts workout={selectedWorkout} />
        </>
      ) : (
        <div className="p-4 w-full flex justify-center">
          <p className="text-2xl">{`Please select a date`}</p>
        </div>
      )}
    </Card>
  );
};

export default WorkoutMetricsDisplay;
