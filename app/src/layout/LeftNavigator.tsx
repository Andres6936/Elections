import {Pressable, Text, View} from "react-native-windows";
import React from "react";
import {useNavigation} from "@react-navigation/native";

export function LeftNavigator() {
    const navigator = useNavigation();

    return (
        <View className="flex-[2] gap-4 p-2">
            <View className="border-b pb-2">
                <Text className="font-semibold">Candidates</Text>
            </View>
            <Pressable onPress={() => navigator.navigate("ElectionsNational")} className="border-b pb-2">
                <Text className="font-semibold">Elections National</Text>
            </Pressable>
            <View className="border-b pb-2">
                <Text className="font-semibold">Elections Native</Text>
            </View>
            <View className="border-b pb-2">
                <Text className="font-semibold">Income Base</Text>
            </View>
            <View className="border-b pb-2">
                <Text className="font-semibold">Items</Text>
            </View>
            <View className="border-b pb-2">
                <Text className="font-semibold">Senator</Text>
            </View>
            <View className="border-b pb-2">
                <Text className="font-semibold">Senator Expenses</Text>
            </View>
        </View>
    )
}