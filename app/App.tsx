import React from 'react';
import {NavigationContainer} from "@react-navigation/native";
import {createNativeStackNavigator} from "@react-navigation/native-stack";
import {CandidateScreen} from "./src/screens/CandidateScreen";

const Stack = createNativeStackNavigator();

export default function App() {
    return (
        <NavigationContainer>
            <Stack.Navigator initialRouteName={"Candidate"}>
                <Stack.Screen name={"Candidate"} component={CandidateScreen}/>
            </Stack.Navigator>
        </NavigationContainer>
    );
}
