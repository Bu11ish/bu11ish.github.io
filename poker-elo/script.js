function main() {
    calculate()
}

function calculate() {
    let inputs = document.getElementsByTagName('input')
    let totalPoints = 0;
    let loserPoints = 0;
    let buyInFactor = 0.1

    for (index = inputs.length-1; index >=0 ; index--) {

        let selfPoints = inputs[index].value * buyInFactor
        let points = -selfPoints
        let selfFactor = Math.pow(2, -index)
        let loserFactor = Math.pow(2, -index-1)

        points += selfPoints * selfFactor + loserPoints * loserFactor

        loserPoints += selfPoints

        let pointsRow = document.getElementById("pointsResultContainer")
        pointsRow.deleteCell(index+1)
        let pointsCell = pointsRow.insertCell(index+1)
        pointsCell.innerHTML = points.toFixed(2)
    }
}
