import { WorkoutLocationTypes } from "./workout_types";

/* ====== Apple Health Records Attributes ====== */
interface AppleHealthRecord {
    type: string;
    unit: string;
    value: string | number;
    sourceName: string;
    sourceVersion: string;
    device: string;
    creationDate: string;
    startDate: string;
    endDate: string;
  }
  
interface AppleHealthHeartRateRecord extends AppleHealthRecord {
    motionContext: string;
  }