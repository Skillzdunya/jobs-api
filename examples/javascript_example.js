// Fetch the latest private jobs from the SkillzDunya Jobs API (Node 18+ or browser).
const url = "https://skillzdunya.com/api/v1/jobs?government=0&sort=newest&per_page=10";

const res = await fetch(url);
const { data } = await res.json();

for (const job of data) {
  console.log(`${job.title} | ${job.url}`);
}
