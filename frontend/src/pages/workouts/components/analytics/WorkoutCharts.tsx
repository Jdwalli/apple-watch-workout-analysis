import React from "react";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";
import WorkoutChart from "./WorkoutChart";
import { WorkoutStats } from "@/types/workout_types";

interface Props {
  workout: WorkoutStats | undefined;
}

const WorkoutCharts: React.FC<Props> = (props: Props) => {
  const { workout } = props;

  const availableCharts = {
    heartRate: workout?.workoutVitals.heartRate.chart != undefined,
    elevation: (workout?.workoutRoute?.elevation?.length ?? 0) > 0,
    speed: (workout?.workoutRoute?.speed?.length ?? 0) > 0,
    runningSpeed: workout?.workoutStatistics?.runningSpeed?.chart?.time
      ? workout.workoutStatistics.runningSpeed.chart.time.length > 0
      : false,
    strideLength: workout?.workoutStatistics?.runningStrideLength?.chart?.time
      ? workout.workoutStatistics.runningStrideLength.chart.time.length > 0
      : false,
    runningPower: workout?.workoutStatistics?.runningPower?.chart?.time
      ? workout.workoutStatistics.runningPower.chart.time.length > 0
      : false,
    groundContactTime: workout?.workoutStatistics?.runningGroundContactTime
      ?.chart?.time
      ? workout.workoutStatistics.runningGroundContactTime.chart.time.length > 0
      : false,
    verticalOscillation: workout?.workoutStatistics?.runningVerticalOscillation
      ?.chart?.time
      ? workout.workoutStatistics.runningVerticalOscillation.chart.time.length >
        0
      : false,
  };

  const availableTabs = Object.entries(availableCharts).filter(
    ([, value]) => value
  );
  const defaultTab = availableTabs[0]?.[0] || "";

  let gridColsClass = "grid-cols-8";
  if (availableTabs.length > 0) {
    gridColsClass = `grid-cols-${availableTabs.length}`;
  }

  return (
    <Tabs defaultValue={defaultTab} className="w-full  overflow-hidden">
      <TabsList className={`grid w-full ${gridColsClass} mb-4`}>
        {availableCharts.heartRate && (
          <TabsTrigger value="heartRate">Heart Rate</TabsTrigger>
        )}

        {availableCharts.elevation && (
          <TabsTrigger value="elevation">Elevation</TabsTrigger>
        )}

        {availableCharts.speed && (
          <TabsTrigger value="speed">Speed</TabsTrigger>
        )}

        {availableCharts.runningSpeed && (
          <TabsTrigger value="runningSpeed">Running Speed</TabsTrigger>
        )}

        {availableCharts.runningPower && (
          <TabsTrigger value="runningPower">Running Power</TabsTrigger>
        )}

        {availableCharts.strideLength && (
          <TabsTrigger value="strideLength">Stride Length</TabsTrigger>
        )}

        {availableCharts.groundContactTime && (
          <TabsTrigger value="groundContactTime">
            Ground Contact Time
          </TabsTrigger>
        )}

        {availableCharts.verticalOscillation && (
          <TabsTrigger value="verticalOscillation">
            Vertical Oscillation
          </TabsTrigger>
        )}
      </TabsList>

      {availableCharts.heartRate && (
        <TabsContent value="heartRate">
          <WorkoutChart
            x={workout?.workoutVitals.heartRate.chart.time ?? []}
            y={workout?.workoutVitals.heartRate.chart.value ?? []}
            yLabel="Heart Rate"
            yUnit={workout?.workoutVitals.heartRate.unit ?? ""}
          />
        </TabsContent>
      )}

      {availableCharts.elevation && (
        <TabsContent value="elevation">
          <WorkoutChart
            x={workout?.workoutRoute.time ?? []}
            y={workout?.workoutRoute.elevation ?? []}
            yLabel="Elevation"
            yUnit={"m"}
          />
        </TabsContent>
      )}

      {availableCharts.speed && (
        <TabsContent value="speed">
          <WorkoutChart
            x={workout?.workoutRoute.time ?? []}
            y={workout?.workoutRoute.speed ?? []}
            yLabel="Speed"
            yUnit={"m/s"}
          />
        </TabsContent>
      )}

      {availableCharts.runningSpeed && (
        <TabsContent value="runningSpeed">
          <WorkoutChart
            x={workout?.workoutStatistics.runningSpeed.chart.time ?? []}
            y={workout?.workoutStatistics.runningSpeed.chart.value ?? []}
            yLabel="Running Speed"
            yUnit={workout?.workoutStatistics.runningSpeed.unit ?? ""}
          />
        </TabsContent>
      )}

      {availableCharts.strideLength && (
        <TabsContent value="strideLength">
          <WorkoutChart
            x={workout?.workoutStatistics.runningStrideLength.chart.time ?? []}
            y={workout?.workoutStatistics.runningStrideLength.chart.value ?? []}
            yLabel="Running Stride Length"
            yUnit={workout?.workoutStatistics.runningStrideLength.unit ?? ""}
          />
        </TabsContent>
      )}

      {availableCharts.runningPower && (
        <TabsContent value="runningPower">
          <WorkoutChart
            x={workout?.workoutStatistics.runningPower.chart.time ?? []}
            y={workout?.workoutStatistics.runningPower.chart.value ?? []}
            yLabel="Power"
            yUnit={workout?.workoutStatistics.runningPower.unit ?? ""}
          />
        </TabsContent>
      )}

      {availableCharts.groundContactTime && (
        <TabsContent value="groundContactTime">
          <WorkoutChart
            x={
              workout?.workoutStatistics.runningGroundContactTime.chart.time ??
              []
            }
            y={
              workout?.workoutStatistics.runningGroundContactTime.chart.value ??
              []
            }
            yLabel="Ground Contact Time"
            yUnit={
              workout?.workoutStatistics.runningGroundContactTime.unit ?? ""
            }
          />
        </TabsContent>
      )}

      {availableCharts.verticalOscillation && (
        <TabsContent value="verticalOscillation">
          <WorkoutChart
            x={
              workout?.workoutStatistics.runningVerticalOscillation.chart
                .time ?? []
            }
            y={
              workout?.workoutStatistics.runningVerticalOscillation.chart
                .value ?? []
            }
            yLabel="Vertical Oscillation"
            yUnit={
              workout?.workoutStatistics.runningVerticalOscillation.unit ?? ""
            }
          />
        </TabsContent>
      )}
    </Tabs>
  );
};

export default WorkoutCharts;
