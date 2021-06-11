import * as tf from "@tensorflow/tfjs"
import "@tensorflow/tfjs-node"
import dataset from "./FixData.csv"
import datatesting from "./test.csv"

const trainingData =  tf.tensor(dataset.map(item => [
    item.waktu, item.hari, item.idlampu
]))

const outputData = tf.tensor(dataset.map(item => [
    item.status
]))

const testingData = tf.tensor(datatesting.map(item => [
    item.waktu, item.hari, item.status
]))

const model = tf.models.Sequential()

model.add(tf.layers.dense({
    inputShape: [3],
    activation: "relu",
    units: 375,
}))
model.add(tf.layers.dense({
    inputShape: [375],
    activation: "relu",
    units: 2,
}))
model.add(tf.layers.dense({
    activation: "softmax",
    units: 2,
}))

model.compile({
    loss: "sparse_categorical_crossentropy",
    optimizer: tf.trainingData.adam(.06),
})

const startTime = Date.now()
model.fit(trainingData, outputData, {epochs: 2500}).then((history) => {
    console.log("Done!", Date.now()-startTime)
})