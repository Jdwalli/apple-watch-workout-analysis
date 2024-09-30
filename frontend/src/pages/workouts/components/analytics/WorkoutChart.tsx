import React from "react";
import { CartesianGrid, Line, LineChart, XAxis, YAxis } from "recharts";
import {
  ChartConfig,
  ChartContainer,
  ChartTooltip,
  ChartTooltipContent,
} from "@/components/ui/chart";

import { format } from "date-fns";

interface Props {
  x: string[];
  y: number[];
  yLabel: string;
  yUnit: string;
}

export const description = "A line chart";

const WorkoutChart: React.FC<Props> = (props: Props) => {
  const chartData = props.x.map((x, index) => {
    return { month: x, y: props.y[index] };
  });

  const chartConfig = {
    y: {
      label: `${props.yLabel} (${props.yUnit}): `,
      color: "hsl(var(--chart-1))",
    },
    x: {
      label: "Timestamp",
      color: "hsl(var(--chart-2))",
    },
  } satisfies ChartConfig;

  const minY = Math.min(...props.y);
  const maxY = Math.max(...props.y);

  const yAxisDomain = [minY, maxY * 1.01];

  return (
    <div className="h-full">
      <ChartContainer
        config={chartConfig}
        className="aspect-auto h-[400px] w-full"
      >
        <LineChart
          accessibilityLayer
          data={chartData}
          margin={{
            left: 12,
            right: 12,
          }}
        >
          <CartesianGrid vertical={false} />
          <XAxis
            dataKey="month"
            tickLine={false}
            axisLine={false}
            tickMargin={8}
            tickFormatter={(value) => format(new Date(value), "HH:mm:ss")}
          />
          <YAxis
            domain={yAxisDomain}
            tickLine={false}
            axisLine={false}
            tickMargin={8}
          />
          <ChartTooltip
            cursor={false}
            content={<ChartTooltipContent hideLabel />}
          />
          <Line
            dataKey="y"
            type="natural"
            stroke="var(--color-y)"
            strokeWidth={2}
            dot={{
              fill: "var(--color-y)",
            }}
            activeDot={{
              r: 2,
            }}
          />
        </LineChart>
      </ChartContainer>
    </div>
  );
};

export default WorkoutChart;
