import http from "k6/http";
import {sleep} from 'k6';

const rampUpStages = [
  { duration: "30s", target: 100 },
  { duration: "60s", target: 100 },
  { duration: "45s", target: 250 },
  { duration: "75s", target: 250 },
  { duration: "60s", target: 500 },
  { duration: "90s", target: 500 },
  { duration: "75s", target: 750 },
  { duration: "120s", target: 750 },
  { duration: "90s", target: 1000 },
  { duration: "180s", target: 1000 },
];

export const options = {
  scenarios: {
    average_load: {
      executor: "ramping-vus",
      stages: rampUpStages,
      gracefulRampDown: "180s",
    },
  },
};

export default function () {
  const BASE_URL = __ENV.BASE_URL;

  if (!BASE_URL) {
    throw new Error("BASE_URL is not defined!");
  }
  const res = http.get(BASE_URL);
  sleep(5);
}
