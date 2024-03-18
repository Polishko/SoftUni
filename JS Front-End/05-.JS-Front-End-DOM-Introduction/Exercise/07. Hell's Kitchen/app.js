function solve() {
   document.querySelector('#btnSend').addEventListener('click', onClick);

   function onClick () {
      let textarea = document.querySelector('textarea');
      let inputArray = JSON.parse(textarea.value);
      let restaurants = {};

      for (const info of inputArray) {
         const [restaurantName, part2] = info.split(' - ');
         
         if (!restaurants.hasOwnProperty(restaurantName)) {
            restaurants[restaurantName] = [];
         }

         const workers = part2.split(', ');
         for (const worker of workers) {
            const [person, wage] = worker.split(' ');
            restaurants[restaurantName].push([person, Number(wage)]);           
         }           
      }

      const wageAverage = (restaurantStaff) => {
         return restaurantStaff.reduce((sum, curr) => sum + curr[1], 0) / restaurantStaff.length;  
      };

      let averageWages = {};
         for (let restName in restaurants) {
            averageWages[restName] = wageAverage(restaurants[restName]);
         }
          
      const bestRestaurant = Object.entries(averageWages).sort((a, b) => b[1] - a[1])[0];

      const bestRestaurantName = bestRestaurant[0];
      const sortedPersonnel = restaurants[bestRestaurantName].sort((a, b) => b[1] - a[1]);
      const personnelInfo = sortedPersonnel.map((personInfo) => `Name: ${personInfo[0]} With Salary: ${parseInt(personInfo[1])}`);

      document.querySelector('#bestRestaurant p').textContent =
       `Name: ${bestRestaurantName} Average Salary: ${averageWages[bestRestaurantName].toFixed(2)} Best Salary: ${sortedPersonnel[0][1].toFixed(2)}`;
      
      document.querySelector('#workers p').textContent = personnelInfo.join(' ');
   }
}

