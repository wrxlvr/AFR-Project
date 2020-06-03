import QtQuick 2.12
import QtQuick.Window 2.12
import QtQuick.Controls.Styles 1.4
import QtQuick.Extras 1.4

Window {
    visible: true
    width: 800
    height: 480
    color: "#000000"
    title: qsTr("AFR Meter")
Recta ngle {
    width: 800
    height: 480
    color: "#ffffff"

    CircularGauge {
        id: circularGauge
        anchors.fill: parent
       // width: 440
        //height: 440
        maximumValue: 24
        style: CircularGaugeStyle{
            labelInset: outerRadius * 0.2
            tickmarkLabel: null
            tickmark: Text {
                text: styleData.value
                Text {
                    anchors.horizontalCenter: parent.horizontalCenter
                    anchors.top: parent.bottom
                    text: styleData.index
                    color: "blue"
                }
            }

            minorTickmark: Text {
                text: styleData.value
                font.pixelSize: 8
                Text {
                    anchors.horizontalCenter: parent.horizontalCenter
                    anchors.top: parent.bottom
                    text: styleData.index
                    font.pixelSize: 8
                    color: "blue"
                }
            }

        }
        Text {
                    id: indexText
                    text: "Major and minor indices"
                    anchors.horizontalCenter: parent.horizontalCenter
                    anchors.bottom: valueText.top
                    color: "blue"
             }
        Text {
                    id: valueText
                    text: "Major and minor values"
                    anchors.horizontalCenter: parent.horizontalCenter
                    anchors.bottom: parent.bottom
             }

    }
}
}
