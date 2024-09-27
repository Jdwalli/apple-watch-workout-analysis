import { Navigate } from "react-router-dom";
import React from "react";

interface ProtectedRouteProps {
  isAllowed: boolean;
  redirectPath?: string;
  children: JSX.Element;
}

const ProtectedRoute: React.FC<ProtectedRouteProps> = ({
  isAllowed,
  redirectPath = "/",
  children,
}) => {
  if (!isAllowed) {
    return <Navigate to={redirectPath} replace />;
  }

  return children;
};

export default ProtectedRoute;
