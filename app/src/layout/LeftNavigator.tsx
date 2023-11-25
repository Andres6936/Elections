import {Pressable, Text, View} from "react-native-windows";
import React from "react";
import {useNavigation} from "@react-navigation/native";

export function LeftNavigator() {
    const navigator = useNavigation();

    return (
        <View className="bg-blue-600 text-white flex-[2] gap-1 p-2">
            <Pressable onPress={() => navigator.navigate("CandidateScreen")} className="p-2 rounded hover:bg-sky-400">
                <Text className="text-white font-semibold">Candidates</Text>
            </Pressable>
            <Pressable onPress={() => navigator.navigate("ElectionsNationalScreen")}
                       className="p-2 rounded hover:bg-sky-400">
                <Text className="text-white font-semibold">Elections National</Text>
            </Pressable>
            <Pressable onPress={() => navigator.navigate("ElectionsNativeScreen")}
                       className="p-2 rounded hover:bg-sky-400">
                <Text className="text-white font-semibold">Elections Native</Text>
            </Pressable>
            <Pressable onPress={() => navigator.navigate("IncomeBaseScreen")} className="p-2 rounded hover:bg-sky-400">
                <Text className="text-white font-semibold">Income Base</Text>
            </Pressable>
            <Pressable onPress={() => navigator.navigate("ItemsScreen")} className="p-2 rounded hover:bg-sky-400">
                <Text className="text-white font-semibold">Items</Text>
            </Pressable>
            <Pressable onPress={() => navigator.navigate("SenatorScreen")} className="p-2 rounded hover:bg-sky-400">
                <Text className="text-white font-semibold">Senator</Text>
            </Pressable>
            <Pressable onPress={() => navigator.navigate("SenatorExpenseScreen")}
                       className="p-2 rounded hover:bg-sky-400">
                <Text className="text-white font-semibold">Senator Expenses</Text>
            </Pressable>
        </View>
    )
}