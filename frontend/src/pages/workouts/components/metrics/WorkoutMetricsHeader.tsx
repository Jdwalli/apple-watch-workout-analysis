import React from "react";
import { WorkoutStats } from "@/types/workout_types";
import { formatWorkoutDates } from "@/helpers/dataFormatting";

interface Props {
  workout: WorkoutStats;
}

const WorkoutMetricsHeader: React.FC<Props> = (props: Props) => {
  return (
    <div className="flex items-center justify-between mt-2 mb-6">
      <div className="flex items-center space-x-4">
        <div>
          <h2 className="text-2xl font-bold">{`${props.workout.workoutMetadata.workoutLocationType} ${props.workout.workoutName}`}</h2>
          <p className="text-sm text-gray-400">
            {formatWorkoutDates(
              props.workout.workoutStartDate,
              props.workout.workoutEndDate,
              props.workout.workoutMetadata.timeZone
            )}
          </p>
        </div>
      </div>
      <div className="text-right">
        <p className="text-3xl font-bold">
          {props.workout.workoutTotalEnergyBurned.toFixed(2)}
        </p>
        <p className="text-sm text-gray-400">Calories Burned</p>
      </div>
    </div>
  );
};

export default WorkoutMetricsHeader;
