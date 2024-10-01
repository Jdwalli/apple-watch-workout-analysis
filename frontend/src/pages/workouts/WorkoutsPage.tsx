import React from "react";
import { useSelector, useDispatch } from "react-redux";
import { RootState } from "../../redux/store";
import { WorkoutApiClient } from "@/clients/workout_clients";
import WorkoutControlPanel from "./WorkoutControlPanel";
import WorkoutMetricsDisplay from "./WorkoutMetricsDisplay";
import { GetWorkoutsByDateParameters } from "@/types/client_types";
import { WorkoutContext } from "@/types/workout_types";
import { updateWorkoutLoadingStatus } from "@/redux/features/workoutLoadingStatusSlice";

const WorkoutsPage: React.FC = () => {
  const workoutClient = new WorkoutApiClient();
  const dispatch = useDispatch();
  const [workoutContext, setWorkoutContext] = React.useState<WorkoutContext>();
  const [loading, setLoading] = React.useState<boolean>(false);

  const selectedWorkoutDate = useSelector(
    (state: RootState) => state.selectedWorkoutDate.selectedWorkoutDate
  );

  React.useEffect(() => {
    const fetchWorkoutData = async () => {
      if (selectedWorkoutDate) {
        setLoading(true);
        try {
          const params: GetWorkoutsByDateParameters = {
            workoutStartDate: selectedWorkoutDate,
          };

          const workoutData = await workoutClient.getWorkoutsByDate(params);
          setWorkoutContext(workoutData.workoutContext);
        } catch (error) {
          console.error("Error fetching workout data:", error);
        } finally {
          setLoading(false);
        }
      } else {
        console.log("No workout date selected, skipping API request.");
      }
    };

    fetchWorkoutData();
  }, [selectedWorkoutDate]); 

  React.useEffect(() => {
    dispatch(updateWorkoutLoadingStatus(loading));
  }, [dispatch, loading]);

  return (
    <div className="container relative h-full flex-col items-center justify-center grid lg:max-w-none grid-cols-[35%,65%] px-0">
      <WorkoutControlPanel workoutContext={workoutContext} />
      <WorkoutMetricsDisplay />
    </div>
  );
};

export default WorkoutsPage;
