import React from "react";
import { WorkoutStats } from "@/types/workout_types";
import {
  Zap,
  Mountain,
  ChartNoAxesGantt,
  MapPinnedIcon,
  Waves,
  SmartphoneCharging,
  Timer,
  Ruler,
  LoaderCircle,
  Footprints,
  Atom,
} from "lucide-react";
import {
  formatWorkoutDate,
  formatWorkoutDuration,
  formatHeartRateValues,
  formatTemperatureValue,
  formatHumidityValue,
  formatWorkoutDistance
} from "@/helpers/dataFormatting";

interface WorkoutPerformanceCategoryProps {
  title: string;
  items: {
    icon: React.ReactNode;
    label: string;
    value: number | string;
    unit: string;
  }[];
}

interface WorkoutTabCardProps {
  icon: React.ReactNode;
  label: string;
  value: string | number;
  unit: string | number;
}
interface ContentProps {
  workout: WorkoutStats;
}

interface DetailsSectionProps {
  title: string;
  children: any;
}

interface DetailsItemsProps {
  label: string;
  value: string;
}

export const WorkoutTabCard: React.FC<WorkoutTabCardProps> = (
  props: WorkoutTabCardProps
) => {
  return (
    <div className="bg-gray-800 p-2 rounded-lg">
      <div className="flex items-center space-x-2 mb-1">
        {props.icon}
        <span className="text-xs text-gray-400">{props.label}</span>
      </div>
      <p className="text-lg font-bold">
        {props.value}{" "}
        <span className="text-xs font-normal text-gray-400">{props.unit}</span>
      </p>
    </div>
  );
};

export const DetailSection: React.FC<DetailsSectionProps> = (
  props: DetailsSectionProps
) => (
  <div className="space-y-2">
    <h3 className="text-lg font-semibold">{props.title}</h3>
    <div className="grid grid-cols-2 gap-4">{props.children}</div>
  </div>
);

export const DetailItem: React.FC<DetailsItemsProps> = (
  props: DetailsItemsProps
) => (
  <div>
    <p className="text-sm text-gray-400">{props.label}</p>
    <p className="font-semibold">{props.value}</p>
  </div>
);

export const WorkoutOverviewContent: React.FC<ContentProps> = (
  props: ContentProps
) => {
  return (
    <div className="space-y-6  h-96 overflow-y-auto pb-12 ">
      <DetailSection title="General Workout Information">
        <DetailItem label="Workout Name" value={props.workout.workoutName} />
        <DetailItem
          label="Location"
          value={props.workout.workoutMetadata.workoutLocationType}
        />
        <DetailItem
          label="Start Date"
          value={formatWorkoutDate(props.workout.workoutStartDate, props.workout.workoutMetadata.timeZone)}
        />
        <DetailItem
          label="End Date"
          value={formatWorkoutDate(props.workout.workoutEndDate, props.workout.workoutMetadata.timeZone)}
        />
        <DetailItem
          label="Duration"
          value={formatWorkoutDuration(props.workout.workoutDuration)}
        />
        <DetailItem
          label="Distance"
          value={`${formatWorkoutDistance(props.workout.workoutTotalDistance)} ${props.workout.workoutTotalDistanceUnit}`}
        />
        <DetailItem
          label="Creation Date"
          value={formatWorkoutDate(props.workout.workoutEndDate, props.workout.workoutMetadata.timeZone)}
        />
        <DetailItem
          label="Time Zone"
          value={props.workout.workoutMetadata.timeZone}
        />
      </DetailSection>

      <DetailSection title="Environmental Conditions">
        <DetailItem
          label="Temperature"
          value={`${formatTemperatureValue(
            props.workout.workoutMetadata.weatherTemperature
          )}`}
        />
        <DetailItem
          label="Humidity"
          value={`${formatHumidityValue(
            props.workout.workoutMetadata.weatherHumidity
          )}`}
        />
        <DetailItem
          label="Water Salinity"
          value={`${props.workout.workoutMetadata.waterSalinity || "-"}`}
        />
      </DetailSection>

      <DetailSection title="Device Information">
        <DetailItem label="Device" value={props.workout.workoutDeviceName} />
        <DetailItem
          label="Route Recorded"
          value={props.workout.workoutRoute.latitude.length > 0 ? "Yes" : "No"}
        />
      </DetailSection>
    </div>
  );
};

const WorkoutPerformanceCategory: React.FC<WorkoutPerformanceCategoryProps> = (
  props: WorkoutPerformanceCategoryProps
) => {
  const validItems = props.items.filter(
    (item) => item.value !== undefined && item.value !== ""
  );

  return (
    <div>
      {validItems.length === 0 ? null : (
        <>
          <h3 className="text-lg font-semibold mb-2">{props.title}</h3>
          <div className="grid grid-cols-2 gap-2">
            {validItems.map((item, index) => (
              <WorkoutTabCard
                key={index}
                icon={item.icon}
                label={item.label}
                value={item.value}
                unit={item.unit}
              />
            ))}
          </div>
        </>
      )}
    </div>
  );
};

export const WorkoutPerformanceContent: React.FC<ContentProps> = (
  props: ContentProps
) => {
  const caloriesItems = [
    {
      icon: <Zap className="h-5 w-5" />,
      label: "Active Energy Burned",
      value: props.workout.workoutStatistics.activeEnergyBurned.sum,
      unit: props.workout.workoutStatistics.activeEnergyBurned.unit,
    },
    {
      icon: <Zap className="h-5 w-5" />,
      label: "Basal Energy Burned",
      value: props.workout.workoutStatistics.basalEnergyBurned.sum,
      unit: props.workout.workoutStatistics.basalEnergyBurned.unit,
    },
  ];

  const mobilityItems = [
    {
      icon: <ChartNoAxesGantt className="h-5 w-5" />,
      label: "Maximum Speed",
      value: props.workout.workoutMetadata.maximumSpeed,
      unit: "meters",
    },
    {
      icon: <ChartNoAxesGantt className="h-5 w-5" />,
      label: "Average Speed",
      value: props.workout.workoutMetadata.averageSpeed,
      unit: "meters",
    },
    {
      icon: <Mountain className="h-5 w-5" />,
      label: "Elevation Ascended",
      value: props.workout.workoutMetadata.elevationAscended,
      unit: "",
    },
    {
      icon: <Mountain className="h-5 w-5" />,
      label: "Elevation Descended",
      value: props.workout.workoutMetadata.elevationDescended,
      unit: "",
    },
    {
      icon: <Footprints className="h-5 w-5" />,
      label: "Distance Walking Running",
      value: props.workout.workoutStatistics.distanceWalkingRunning.sum,
      unit: props.workout.workoutStatistics.distanceWalkingRunning.unit,
    },
    {
      icon: <Footprints className="h-5 w-5" />,
      label: "Step Count",
      value: props.workout.workoutStatistics.stepCount.sum,
      unit: props.workout.workoutStatistics.stepCount.unit,
    },
  ];

  const swimmingItems = [
    {
      icon: <MapPinnedIcon className="h-5 w-5" />,
      label: "Swimming Location Type",
      value: props.workout.workoutMetadata.swimmingLocationType,
      unit: "",
    },
    {
      icon: <Waves className="h-5 w-5" />,
      label: "Swimming Stroke Style",
      value: props.workout.workoutMetadata.swimmingStrokeStyle,
      unit: "",
    },
    {
      icon: <Ruler className="h-5 w-5" />,
      label: "Swimming Lap Length",
      value: props.workout.workoutMetadata.lapLength,
      unit: "",
    },
    {
      icon: <Waves className="h-5 w-5" />,
      label: "Swimming SWOLF Score",
      value: props.workout.workoutMetadata.swolfScore,
      unit: "",
    },
    {
      icon: <Atom className="h-5 w-5" />,
      label: "Water Salinity",
      value: props.workout.workoutMetadata.waterSalinity,
      unit: "",
    },
    {
      icon: <Waves className="h-5 w-5" />,
      label: "Swimming Stroke Count",
      value: props.workout.workoutStatistics.swimmingStrokeCount.sum,
      unit: props.workout.workoutStatistics.swimmingStrokeCount.unit,
    },
    {
      icon: <Waves className="h-5 w-5" />,
      label: "Distance Swimming",
      value: props.workout.workoutStatistics.distanceSwimming.sum,
      unit: props.workout.workoutStatistics.distanceSwimming.unit,
    },
  ];

  const runningItems = [
    {
      icon: <Timer className="h-5 w-5" />,
      label: "Average Running Ground Contact Time",
      value: props.workout.workoutStatistics.runningGroundContactTime.average,
      unit: props.workout.workoutStatistics.runningGroundContactTime.unit,
    },
    {
      icon: <SmartphoneCharging className="h-5 w-5" />,
      label: "Average Running Power",
      value: props.workout.workoutStatistics.runningPower.average,
      unit: props.workout.workoutStatistics.runningPower.unit,
    },
    {
      icon: <LoaderCircle className="h-5 w-5" />,
      label: "Average Running Vertical Oscillation",
      value: props.workout.workoutStatistics.runningVerticalOscillation.average,
      unit: props.workout.workoutStatistics.runningVerticalOscillation.unit,
    },
    {
      icon: <ChartNoAxesGantt className="h-5 w-5" />,
      label: "Average Running Speed",
      value: props.workout.workoutStatistics.runningSpeed.average,
      unit: props.workout.workoutStatistics.runningSpeed.unit,
    },
    {
      icon: <Ruler className="h-5 w-5" />,
      label: "Average Running Stride Length",
      value: props.workout.workoutStatistics.runningStrideLength.average,
      unit: props.workout.workoutStatistics.runningStrideLength.unit,
    },
  ];

  return (
    <div className="max-h-[calc(100vh-200px)] h-96 space-y-6 overflow-y-auto pb-12 pr-4">
      <WorkoutPerformanceCategory title="Calories" items={caloriesItems} />
      <WorkoutPerformanceCategory title="Mobility" items={mobilityItems} />
      <WorkoutPerformanceCategory title="Swimming" items={swimmingItems} />
      <WorkoutPerformanceCategory title="Running" items={runningItems} />
    </div>
  );
};

export const WorkoutVitalsContent: React.FC<ContentProps> = (
  props: ContentProps
) => {
  return (
    <div className="space-y-6  h-96 overflow-y-auto pb-12 ">
      <DetailSection title="Vitals">
        <DetailItem
          label="Avg Heart Rate"
          value={`${formatHeartRateValues(
            props.workout.workoutStatistics.heartRate.average
          )} BPM`}
        />
        <DetailItem
          label="Min Heart Rate"
          value={`${formatHeartRateValues(
            props.workout.workoutStatistics.heartRate.minimum
          )} BPM`}
        />
        <DetailItem
          label="Max Heart Rate"
          value={`${formatHeartRateValues(
            props.workout.workoutStatistics.heartRate.maximum
          )} BPM`}
        />
        <DetailItem
          label="Average Mets"
          value={`${props.workout.workoutMetadata.averageMETs}`}
        />
      </DetailSection>
    </div>
  );
};
