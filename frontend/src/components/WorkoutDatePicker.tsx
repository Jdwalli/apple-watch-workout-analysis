import * as React from "react";
import { Calendar as CalendarIcon } from "lucide-react";

import { cn } from "@/lib/utils";
import { Button } from "@/components/ui/button";
import { Calendar } from "@/components/ui/calendar";
import {
  Popover,
  PopoverContent,
  PopoverTrigger,
} from "@/components/ui/popover";
import { format, parseISO, isSameDay } from "date-fns";

interface Props {
  workoutDates: string[];
}

const WorkoutDatePicker: React.FC<Props> = (props: Props) => {
  const [date, setDate] = React.useState<Date>();
  const enabledDates = props.workoutDates.map((date) => parseISO(date));

  const isValidWorkoutDate = (day: Date) =>
    enabledDates.some((enabledDate) => isSameDay(day, enabledDate));


  const handleDateSelect = (selectedDate: Date | undefined) => {
        setDate(selectedDate)
        if (selectedDate) {
          console.log("Selected workout date:", format(selectedDate, "yyyy-MM-dd"))
        }
      }
    
  return (
    <Popover>
      <PopoverTrigger asChild>
        <Button
          variant={"outline"}
          className={cn(
            "w-[280px] justify-start text-left font-normal",
            !date && "text-muted-foreground"
          )}
        >
          <CalendarIcon className="mr-2 h-4 w-4" />
          {date ? format(date, "PPP") : <span>Pick a workout date</span>}
        </Button>
      </PopoverTrigger>
      <PopoverContent className="w-auto p-0">
        <Calendar
          mode="single"
          selected={date}
          onSelect={handleDateSelect}
          modifiers={{
            disabled: (day) => !isValidWorkoutDate(day),
          }}
          initialFocus
          defaultMonth={enabledDates[props.workoutDates.length - 1]}
          fromDate={enabledDates[0]}
          toDate={enabledDates[props.workoutDates.length - 1]}
          className="custom-calendar"
        />
      </PopoverContent>
    </Popover>
  );
};

export default WorkoutDatePicker;
