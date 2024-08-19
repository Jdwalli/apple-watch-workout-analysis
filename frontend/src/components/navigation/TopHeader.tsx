import React from "react";
import Button from "../common/Button";

const TopHeader: React.FC = () => {
  return (
    <div className="bg-[#1E1F25] h-16 w-full px-4 flex items-center justify-between">
			<div className="relative">
				<span className="font-bold text-white text-lg">
					Apple Watch Workouts
				</span>
			</div>
			<Button text="Upload" variant="primary" />
		</div>
  );
};

export default TopHeader;