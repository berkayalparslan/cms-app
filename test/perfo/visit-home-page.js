import http from "k6/http";

const rampUpStages = [
  { duration: "5s", target: 50 },
  { duration: "20s", target: 50 },
  { duration: "15s", target: 250 },
  { duration: "40s", target: 250 },
  { duration: "20s", target: 500 },
  { duration: "80s", target: 500 },
  { duration: "40s", target: 1000 },
  { duration: "120s", target: 1000 },
  { duration: "60s", target: 2500 },
  { duration: "160s", target: 2500 },
  { duration: "120s", target: 5000 },
  { duration: "180s", target: 5000 },
  { duration: "240s", target: 10000 },
  { duration: "300s", target: 10000 },
];

export const options = {
  scenarios: {
    average_load: {
      executor: "ramping-vus",
      stages: [
        { duration: "15s", target: 5000 },
        { duration: "75s", target: 5000 },
      ],
      gracefulRampDown: "120s",
    },
  },
};

export default function () {
  const BASE_URL = __ENV.BASE_URL;

  if (!BASE_URL) {
    throw new Error("BASE_URL is not defined!");
  }
  const res = http.get(BASE_URL);
}
