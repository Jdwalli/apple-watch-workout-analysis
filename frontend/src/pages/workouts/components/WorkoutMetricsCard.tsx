interface Props {
  icon: React.ReactNode;
  label: string;
  value: string | number;
  unit: string | number;
}

const WorkoutMetricsCard: React.FC<Props> = (props: Props) => {
  return (
    <div className="bg-gray-800 p-4 rounded-lg flex items-center space-x-4">
    {props.icon}
    <div>
      <p className="text-sm text-gray-400">{props.label}</p>
      <p className="text-lg font-semibold">{props.value} {props.unit}</p>
    </div>
  </div>
  );
};

export default WorkoutMetricsCard;
