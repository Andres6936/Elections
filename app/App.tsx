import React from 'react';
import {NavigationContainer} from "@react-navigation/native";
import {createNativeStackNavigator} from "@react-navigation/native-stack";
import {CandidateScreen} from "./src/screens/CandidateScreen";
import {ElectionsNationalScreen} from "./src/screens/ElectionsNationalScreen";
import {ElectionsNativeScreen} from "./src/screens/ElectionsNativeScreen";
import {IncomeBaseScreen} from "./src/screens/IncomeBaseScreen";
import {SenatorExpenseScreen} from "./src/screens/SenatorExpenseScreen";
import {SenatorScreen} from "./src/screens/SenatorScreen";
import {ItemsScreen} from "./src/screens/ItemsScreen";

const Stack = createNativeStackNavigator();

export default function App() {
    return (
        <NavigationContainer>
            <Stack.Navigator initialRouteName={"CandidateScreen"}>
                <Stack.Screen name={"CandidateScreen"} component={CandidateScreen}/>
                <Stack.Screen name={"ElectionsNationalScreen"} component={ElectionsNationalScreen}/>
                <Stack.Screen name={"ElectionsNativeScreen"} component={ElectionsNativeScreen}/>
                <Stack.Screen name={"IncomeBaseScreen"} component={IncomeBaseScreen}/>
                <Stack.Screen name={"ItemsScreen"} component={ItemsScreen}/>
                <Stack.Screen name={"SenatorExpenseScreen"} component={SenatorExpenseScreen}/>
                <Stack.Screen name={"SenatorScreen"} component={SenatorScreen}/>
            </Stack.Navigator>
        </NavigationContainer>
    );
}
