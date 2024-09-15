import ApiClient from "./api_clients";
import { GetWorkoutsByDateParameters, WorkoutResponse, WorkoutDetailsResponse } from "../types/client_types";

export class WorkoutApiClient {
  apiClient = new ApiClient();
  HEADERS = {
    "Content-Type": "application/json"
  }

  async getWorkoutDetails(): Promise<WorkoutDetailsResponse> {
    try {
      const response = await this.apiClient.request({
        httpMethod: 'GET',
        path: '/api/workout-details',
      });
      return response.data;
    } catch (error) {
      console.error("Error:", error);
      throw error;
    }
  }
  

  async getWorkoutsByDate(params: GetWorkoutsByDateParameters): Promise<WorkoutResponse> {
    try {
      const response = await this.apiClient.request({
        httpMethod: 'POST',
        path: '/api/workout',
        headers: this.HEADERS,
        body: params
      });
      return response.data;
    } catch (error) {
      console.error("Error:", error);
      throw error;
    }
  }


}