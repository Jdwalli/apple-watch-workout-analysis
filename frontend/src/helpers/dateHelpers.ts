import { format, parseISO } from 'date-fns';


export const formatWorkoutDates = (startDate: string, endDate: string): string => {
    const workoutStart = parseISO(startDate.trim().split(' - ')[0].slice(0, -6))
    const workoutEnd = parseISO(endDate.trim().split(' - ')[0].slice(0, -6))

    const formattedStartDate = format(workoutStart, "h:mm a");
    const formattedEndDate = format(workoutEnd, "h:mm a");

    return `${formattedStartDate} - ${formattedEndDate}`;
}