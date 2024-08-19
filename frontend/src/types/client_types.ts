
export interface ApiClientRequest {
    httpMethod: "GET" | "POST";
    path: string;
    body?: any;
    queryParams?: any;
    headers?: any;
  }
  
  