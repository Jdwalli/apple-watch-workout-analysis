import React from "react";
import { WorkoutStats } from "@/types/workout_types";
import WorkoutMetricsCard from "../WorkoutMetricsCard";
import {
  formatWorkoutDuration,
  formatWorkoutDistance,
  formatHeartRateValues,
} from "@/helpers/dataFormatting";
import { Clock, MapPin, Droplets, Heart } from "lucide-react";

interface Props {
  workout: WorkoutStats;
}

const WorkoutMetricsDefaultCards: React.FC<Props> = (props: Props) => {
  let distance = 0;
  let distanceUnit = "";

  switch (props.workout.workoutName) {
    case "Swimming":
      distance = props.workout.workoutStatistics.distanceSwimming.sum;
      distanceUnit = props.workout.workoutStatistics.distanceSwimming.unit;
      break;
    case "Cycling":
      distance = props.workout.workoutStatistics.distanceCycling.sum;
      distanceUnit = props.workout.workoutStatistics.distanceCycling.unit;
      break;
    default:
      distance = props.workout.workoutTotalDistance;
      distanceUnit = props.workout.workoutTotalDistanceUnit;
      break;
  }

  return (
    <div className="grid grid-cols-2 gap-4 mb-6">
      <WorkoutMetricsCard
        icon={<Clock className="h-5 w-5" />}
        label="Workout Duration"
        value={formatWorkoutDuration(props.workout.workoutDuration)}
        unit={""}
      />
      <WorkoutMetricsCard
        icon={<MapPin className="h-5 w-5" />}
        label="Distance"
        value={formatWorkoutDistance(distance)}
        unit={distanceUnit}
      />

      <WorkoutMetricsCard
        icon={<Droplets className="h-5 w-5" />}
        label="Avg METs"
        value={`${props.workout.workoutMetadata.averageMETs}`}
        unit={""}
      />
      <WorkoutMetricsCard
        icon={<Heart className="h-5 w-5" />}
        label="Average Heart Rate"
        value={formatHeartRateValues(
          props.workout.workoutStatistics.heartRate.average,
          "BPM"
        )}
        unit={""}
      />
    </div>
  );
};

export default WorkoutMetricsDefaultCards;
