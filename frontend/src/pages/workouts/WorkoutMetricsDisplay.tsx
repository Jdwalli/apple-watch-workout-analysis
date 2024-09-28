import * as React from "react";
import { Card } from "@/components/ui/card";

import WorkoutMap from "./components/analytics/WorkoutMap";
import WorkoutCharts from "./components/analytics/WorkoutCharts";

interface Props {}

const WorkoutMetricsDisplay: React.FC<Props> = (props: Props) => {
  return (
    <Card className="w-full h-full">
      <WorkoutMap />
      <WorkoutCharts />
    </Card>
  );
};

export default WorkoutMetricsDisplay;
