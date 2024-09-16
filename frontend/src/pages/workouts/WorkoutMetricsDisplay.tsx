import * as React from "react";
import WorkoutPicker from "./components/WorkoutPicker";
import WorkoutMetadataOutput from "./components/WorkoutMetadataOutput";

interface Props {
  
}

const WorkoutMetricsDisplay: React.FC<Props> = (props: Props) => {
  return (
    <div className="h-full">
        <WorkoutPicker />
        <WorkoutMetadataOutput />
    </div>
  );
};

export default WorkoutMetricsDisplay;
