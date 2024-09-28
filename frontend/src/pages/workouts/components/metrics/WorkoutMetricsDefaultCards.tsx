import React from "react";
import { WorkoutStats } from "@/types/workout_types";
import WorkoutMetricsCard from "../WorkoutMetricsCard";
import { formatWorkoutDuration } from "@/helpers/dataFormatting";
import { Clock, MapPin, Droplets, Heart } from "lucide-react";

interface Props {
  workout: WorkoutStats;
}

const WorkoutMetricsDefaultCards: React.FC<Props> = (props: Props) => {
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
        value={props.workout.workoutTotalDistance.toFixed(2)}
        unit={props.workout.workoutTotalDistanceUnit}
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
        value={Math.round(props.workout.workoutStatistics.heartRate.average)}
        unit={"BPM"}
      />
    </div>
  );
};

export default WorkoutMetricsDefaultCards;
