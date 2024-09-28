import React from "react";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";
import { WorkoutStats } from "@/types/workout_types";
import {
  WorkoutOverviewContent,
  WorkoutVitalsContent,
  WorkoutPerformanceContent,
} from "./tabs/WorkoutTabsContent";

interface Props {
  workout: WorkoutStats;
}

const WorkoutMetricsTabs: React.FC<Props> = (props: Props) => {
  return (
    <Tabs defaultValue="overview" className="w-full">
      <TabsList className="grid w-full grid-cols-3 mb-4">
        <TabsTrigger value="overview">Workout Overview</TabsTrigger>
        <TabsTrigger value="performance">Workout Performance</TabsTrigger>
        <TabsTrigger value="vitals">Workout Vitals</TabsTrigger>
      </TabsList>
      <TabsContent value="overview">
        <WorkoutOverviewContent workout={props.workout} />
      </TabsContent>
      <TabsContent value="performance">
        <WorkoutPerformanceContent workout={props.workout} />
      </TabsContent>
      <TabsContent value="vitals">
        <WorkoutVitalsContent workout={props.workout} />
      </TabsContent>
    </Tabs>
  );
};

export default WorkoutMetricsTabs;
