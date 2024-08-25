import React from "react";
import Button from "../common/Button";
import { useNavigate } from "react-router-dom";

const TopHeader: React.FC = () => {
	const navigate = useNavigate();
  return (
    <div className="bg-[#1E1F25] h-16 w-full px-4 flex items-center justify-between">
			<div className="relative">
				<span className="font-bold text-white text-lg">
					Apple Watch Workouts
				</span>
			</div>
			<Button text="Upload" variant="primary" onClick={() => navigate("/")}  />
		</div>
  );
};

export default TopHeader;