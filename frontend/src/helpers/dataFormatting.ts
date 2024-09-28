import { format, parseISO } from "date-fns";


const parseInputValue = (input: string | number, suffix?: string): string => {
  if (typeof input === 'string') {
    if (input === "") {
      return "-";
    }
    return input;
  }

  if (typeof input === 'number') {
    return suffix ? `${Math.round(input)}${suffix}` : Math.round(input).toString();
  }

  return "";
};

export const formatWorkoutDuration = (durationInMinutes: number): string => {
  const totalSeconds = Math.round(durationInMinutes * 60);
  const hours = Math.floor(totalSeconds / 3600);
  const minutes = Math.floor((totalSeconds % 3600) / 60);
  const seconds = totalSeconds % 60;

  return `${String(hours).padStart(2, "0")}:${String(minutes).padStart(
    2,
    "0"
  )}:${String(seconds).padStart(2, "0")}`;
};

export const formatWorkoutDates = (
  startDate: string,
  endDate: string
): string => {
  const workoutStart = parseISO(startDate.trim().split(" - ")[0].slice(0, -6));
  const workoutEnd = parseISO(endDate.trim().split(" - ")[0].slice(0, -6));

  const formattedStartDate = format(workoutStart, "h:mm a");
  const formattedEndDate = format(workoutEnd, "h:mm a");

  return `${formattedStartDate} - ${formattedEndDate}`;
};

export const formatWorkoutDistance = (workoutDistance: string | number): string => {
  const formattedValue = parseInputValue(workoutDistance);
  console.log(formattedValue)
  if (formattedValue !== "-" && typeof workoutDistance === 'number') {
        return workoutDistance.toFixed(2).toString();
  }
  return formattedValue;
};

export const formatHeartRateValues = (heartRate: string | number): string => {
  return parseInputValue(heartRate);
};

export const formatTemperatureValue = (temperature: string | number): string => {
  if (typeof temperature === "string") {
    if (temperature === "") {
      return "-";
    }

    const match = temperature.match(/^(\d+(\.\d+)?)\s*(degF|degC)$/);
    if (match) {
      const value = parseFloat(match[1]);
      const unit = match[3];
      return `${Math.round(value)} ${unit === 'degF' ? '°F' : '°C'}`;
    }

    return temperature;
  }

  return `${Math.round(temperature)} °F`;
};

export const formatHumidityValue = (humidity: string | number): string => {
  return parseInputValue(humidity, "%");
};