import {
  MapContainer,
  Polyline,
  TileLayer,
  useMap,
  Circle,
} from "react-leaflet";
import React from "react";
import "leaflet/dist/leaflet.css";

interface ViewProps {
  center: [number, number];
  zoom: number;
}

interface Props {
  lat: number[];
  long: number[];
}

const ChangeView: React.FunctionComponent<ViewProps> = (props: ViewProps) => {
  const map = useMap();
  map.setView(props.center, props.zoom);
  return null;
};

const calculateMapCenterAndZoom = (lat: number[], long: number[]) => {
  if (lat.length === 0 || long.length === 0) {
    return { center: [0, 0] as [number, number], zoom: 3 };
  }

  const bounds = [
    [Math.min(...lat), Math.min(...long)],
    [Math.max(...lat), Math.max(...long)],
  ];

  const center: [number, number] = [
    (bounds[0][0] + bounds[1][0]) / 2,
    (bounds[0][1] + bounds[1][1]) / 2,
  ];

  const zoom = Math.round(Math.log2(360 / (bounds[1][1] - bounds[0][1]))) + 1;

  return { center, zoom };
};

const WorkoutMap: React.FC<Props> = (props: Props) => {
  const defaultCenter: [number, number] = [0, 0];
  const defaultZoom = 3;

  const { lat, long } = props;
  const hasCoordinates = lat.length > 0 && long.length > 0;
  const { center, zoom } = hasCoordinates
    ? calculateMapCenterAndZoom(lat, long)
    : { center: defaultCenter, zoom: defaultZoom };

  const zippedCords = hasCoordinates ? lat.map((x, i) => [x, long[i]]) : [];

  return (
    <MapContainer
      style={{
        height: "350px",
        width: "100%",
      }}
      center={center}
      zoom={zoom}
      minZoom={3}
      scrollWheelZoom={true}
      zoomControl={true}
      dragging={true}
    >
      {hasCoordinates ? (
        <>
          <ChangeView center={center} zoom={zoom} />
          <TileLayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" />
          <Polyline
            pathOptions={{ fillColor: "red", color: "blue", weight: 5 }}
            positions={zippedCords as [number, number][]}
          />
          <Circle
            center={[lat[0], long[0]]}
            radius={8}
            pathOptions={{ color: "white", fillColor: "green", fillOpacity: 1 }}
          />
          <Circle
            center={[lat[lat.length - 1], long[long.length - 1]]}
            radius={8}
            pathOptions={{ color: "white", fillColor: "red", fillOpacity: 1 }}
          />
        </>
      ) : (
        <div>
          <ChangeView center={center} zoom={zoom} />
          <TileLayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" />
        </div>
      )}
    </MapContainer>
  );
};

export default WorkoutMap;
