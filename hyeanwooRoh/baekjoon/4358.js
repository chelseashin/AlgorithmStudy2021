// 생태학
// 17분

// const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const input = ['Red Alder','Ash','Aspen','Basswood','Ash','Beech','Yellow Birch','Ash','Cherry','Cottonwood','Ash','Cypress','Red Elm','Gum','Hackberry','White Oak','Hickory','Pecan','Hard Maple','White Oak','Soft Maple','Red Oak','Red Oak','White Oak','Poplan','Sassafras','Sycamore','Black Walnut','Willow'];

function solve() {
  const trees = {};
  const nameSet = new Set();
  input.forEach(t => {
    if (trees[t] === undefined) {
      trees[t] = 1;
    } else {
      trees[t]++;
    }
    nameSet.add(t);
  })

  const sortName = [...nameSet].sort();
  sortName.forEach(name => {
    const percentage = ((trees[name]/input.length)*100).toFixed(4);
    console.log(name + ' ' + percentage)
  });
}

solve();
