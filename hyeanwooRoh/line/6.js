// 02:14:50 ~ 02:58:00 44분

// company구조와 applicant구조에서 좀 헤맴

const c = [
  ["A fabdec 2", "B cebdfa 2", "C ecfadb 2"],
  ["A abc 2", "B abc 1"],
]
const a = [
  ["a BAC 1", "b BAC 3", "c BCA 2", "d ABC 3", "e BCA 3", "f ABC 2"],
  ["a AB 1", "b AB 1", "c AB 1"],
]

function solve(company, applicant) {
  const companyList = {};
  const person = [];
  const coms = {};
  company.forEach(v => { // company 초기화
    const [name, apps, hireCnt] = v.split(' ');
    coms[name] = {
      apps,
      hireCnt: hireCnt*1,
    }
    companyList[name] = [];
  })

  const apps = {};
  applicant.forEach(v => { // applicant 초기화
    const [name, coms, applyCnt] = v.split(' ');
    apps[name] = {
      coms,
      applyCnt: applyCnt*1,
      patience: 0,
    }
    person.push(name);
  })

  while (person.length !== 0) {
    // 회사에 지원자 추가
    while (person.length !== 0) {
      const name = person.pop();
      if (apps[name].applyCnt !== 0) {
        const comName = apps[name].coms.charAt(apps[name].patience);
        companyList[comName].push(name);
        apps[name].applyCnt--;
        apps[name].patience++;
      }
    }

    // 회사에서 거르기
    for (const comName of Object.keys(companyList)) {
      const { apps, hireCnt } = coms[comName];
      if (companyList[comName].length > hireCnt) {
        companyList[comName].sort((a,b) => apps.indexOf(a) - apps.indexOf(b));
        const failPerson = companyList[comName].splice(hireCnt);
        person.push(...failPerson);
      }
    }
  }

  return Object.keys(companyList).map(v => {
    return v + '_' + companyList[v].sort().join('');
  });
}

for (const idx in c) {
  console.log(solve(c[idx], a[idx]));
}