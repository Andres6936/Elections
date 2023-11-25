import {Pressable, Text, View} from "react-native-windows";
import React from "react";
import {useNavigation} from "@react-navigation/native";

export function LeftNavigator() {
    const navigator = useNavigation();

    return (
        <View className="flex-[2] gap-4 p-2">
            <Pressable onPress={() => navigator.navigate("CandidateScreen")} className="border-b pb-2">
                <Text className="font-semibold">Candidates</Text>
            </Pressable>
            <Pressable onPress={() => navigator.navigate("ElectionsNationalScreen")} className="border-b pb-2">
                <Text className="font-semibold">Elections National</Text>
            </Pressable>
            <Pressable onPress={() => navigator.navigate("ElectionsNativeScreen")} className="border-b pb-2">
                <Text className="font-semibold">Elections Native</Text>
            </Pressable>
            <Pressable onPress={() => navigator.navigate("IncomeBaseScreen")} className="border-b pb-2">
                <Text className="font-semibold">Income Base</Text>
            </Pressable>
            <Pressable onPress={() => navigator.navigate("ItemsScreen")} className="border-b pb-2">
                <Text className="font-semibold">Items</Text>
            </Pressable>
            <Pressable onPress={() => navigator.navigate("SenatorScreen")} className="border-b pb-2">
                <Text className="font-semibold">Senator</Text>
            </Pressable>
            <Pressable onPress={() => navigator.navigate("SenatorExpenseScreen")} className="border-b pb-2">
                <Text className="font-semibold">Senator Expenses</Text>
            </Pressable>
        </View>
    )
}