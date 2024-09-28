import React from "react";
import WorkoutDatePicker from "@/components/WorkoutDatePicker";
import { CardHeader } from "@/components/ui/card";
import { WorkoutApiClient } from "@/clients/workout_clients";
import { WorkoutDetailsContext } from "@/types/workout_types";
import { WorkoutContext } from "@/types/workout_types";
import { Button } from "@/components/ui/button";
import { ArrowLeft, ArrowRight } from "lucide-react";
import { useDispatch } from "react-redux";
import { updateSelectedWorkout } from "@/redux/features/selectedWorkoutSlice";

interface Props {
  workoutData: WorkoutContext | undefined;
}

const WorkoutPicker: React.FC<Props> = (props: Props) => {
  const dispatch = useDispatch();
  const workoutClient = new WorkoutApiClient();
  const workouts = React.useMemo(() => props.workoutData?.workouts ?? [], [props.workoutData]);
  const totalWorkouts = workouts.length;
  const [workoutDetails, setWorkoutDetails] =
    React.useState<WorkoutDetailsContext>();
  const [currentIndex, setCurrentIndex] = React.useState(0);

  React.useEffect(() => {
    const fetchWorkoutDetails = async () => {
      try {
        const workoutData = await workoutClient.getWorkoutDetails();
        setWorkoutDetails(workoutData.workoutDetailsContext);
      } catch (error) {
        console.error("Error fetching workout data:", error);
      }
    };

    fetchWorkoutDetails();
  }, []);

  React.useEffect(() => {
    if (workouts.length > 0) {
      dispatch(
        updateSelectedWorkout({
          workout: workouts[currentIndex],
        })
      );
    }
  }, [currentIndex, workouts, dispatch]);

  const handlePrevious = () => {
    setCurrentIndex((prevIndex) =>
      prevIndex > 0 ? prevIndex - 1 : workouts.length - 1
    );
  };

  const handleNext = () => {
    setCurrentIndex((prevIndex) =>
      prevIndex < workouts.length - 1 ? prevIndex + 1 : 0
    );
  };

  return (
    <CardHeader className="p-2">
      <div className="flex justify-between items-start">
        <div className="flex items-center">
          <Button
            variant="outline"
            size="icon"
            onClick={handlePrevious}
            disabled={workouts.length == 0}
            className={`mr-2 ${
              workouts.length === 0 ? "cursor-not-allowed" : "pointer"
            }`}
          >
            <ArrowLeft className="h-4 w-4" />
          </Button>

          <div className="text-center min-w-[100px]">
            {workouts.length > 0 ? (
              <span className="text-xs text-zinc-400">
                <p className="text-lg font-bold text-primary">
                  Workout {currentIndex + 1}
                </p>
                <p className="text-sm text-muted-foreground">
                  of {totalWorkouts}
                </p>
              </span>
            ) : (
              <p className="text-lg font-bold text-primary">N / A </p>
            )}
          </div>

          <Button
            variant="outline"
            size="icon"
            onClick={handleNext}
            disabled={workouts.length == 0}
            className={`ml-2 ${
              workouts.length === 0 ? "cursor-not-allowed" : "pointer"
            }`}
          >
            <ArrowRight className="h-4 w-4" />
          </Button>
        </div>
        <div className="flex items-center space-x-2">
          <span className="text-xs text-zinc-400">
            <WorkoutDatePicker
              workoutDates={workoutDetails?.workoutDates ?? []}
            />
          </span>
        </div>
      </div>
    </CardHeader>
  );
};

export default WorkoutPicker;
