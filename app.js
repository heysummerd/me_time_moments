console.log("Hello World!");

// collect user input
userChoices = surveyInput();

// Load data from Supabase
loadDates();

async function loadDates() {
  const res = await fetch(
    "https://pobpjfoiuovltaufdtut.supabase.co/rest/v1/date_ideas",
    {
      headers: {
        apikey:
          "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InBvYnBqZm9pdW92bHRhdWZkdHV0Iiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTc5MDY0NTUsImV4cCI6MjAxMzQ4MjQ1NX0.ObLebjiWxoC9TdWhMGKU6gerIeDIrHtlZ_euSCMIM_0",
        authorization:
          "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InBvYnBqZm9pdW92bHRhdWZkdHV0Iiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTc5MDY0NTUsImV4cCI6MjAxMzQ4MjQ1NX0.ObLebjiWxoC9TdWhMGKU6gerIeDIrHtlZ_euSCMIM_0",
      },
    }
  );
  const data = await res.json();
  console.log(data);

  /** const filteredData = filterData(userChoices, data)
  
  // 

  printDateIdea(filteredData); (Section 5 - 48) 

  **/
}

// function filterData(userChoices, data) {}

function surveyInput() {
  // create userChoice object
  userChoicesObj = {};
  // question 1

  // question 2
  // question 3
  // question 4
  // question 5
}

function printDateIdea(dateObj) {
  let activity = dateObj["activity_name"];
  let ampm = dateObj["time_of_day"];
  let cost = dateObj["cost"];
  let inout = dateObj["indoor_outdoor"];
  let energy = dateObj["energy_level"];
  let length = dateObj["time_length"];
  let purpose = dateObj["purpose"];
  let description = dateObj["description"];

  return ` your ${purpose} date details:
          enjoy a ${activity} :) 
          ${description}`;
}

/** const dateObj = {
  activity_name: "Picnic",
  time_of_day: "flexible",
  cost: "cheap",
  indoor_outdoor: "outdoor",
  energy_level: "light",
  time_length: "flexible",
  purpose: "excitement",
  description: "Gather up a few food items and find a pretty spot!",
  createSummary: function () {
    return `Your date idea: ${this.activity_name} \n ${this.description}`;
  },
}; **/

