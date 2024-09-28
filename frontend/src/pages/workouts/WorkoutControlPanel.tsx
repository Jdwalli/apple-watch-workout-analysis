import React from "react";
import { Card } from "@/components/ui/card";
import WorkoutPicker from "./components/WorkoutPicker";
import WorkoutMetadataOutput from "./components/WorkoutMetadataOutput";
import { WorkoutContext } from "@/types/workout_types";

interface Props {
  workoutContext: WorkoutContext | undefined;
}

const WorkoutControlPanel: React.FC<Props> = (props: Props) => {
  return (
    <Card className="w-full h-full overflow-hidden">
      <WorkoutPicker workoutData={props.workoutContext} />
      <WorkoutMetadataOutput />
    </Card>
  );
};

export default WorkoutControlPanel;
