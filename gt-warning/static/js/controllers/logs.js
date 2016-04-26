angular.module('gtWarning')
    .controller('LogCtrl', function ($scope, $rootScope, $http, $state) {
        $scope.LogMember = [

        ];
        $scope.numbers = [

        ];
        $scope.viewNumber = [1,2,3,4,5,6,7,8];
        $scope.left = undefined;
        $scope.right = undefined;
        $scope.MemberLength = undefined;
        var changeNumber = function(page){
            if(page == $scope.viewNumber[7]){
                for(var i = 0; i<=7 ;i++){
                    if($scope.viewNumber[7] == $scope.numbers[$scope.numbers.length-1])
                        break;
                    $scope.viewNumber[i] += 2;
                }
            }
            if(page == $scope.viewNumber[0] && page != 1){
                for(var i = 0; i<=7 ;i++){
                    if($scope.viewNumber[7] == 8)
                        break;
                    $scope.viewNumber[i] -= 2;
                }
            }
        };
        $scope.head = function(){
            var current = $scope.page;
            if(current != 1){
                $scope.pageMessage(current-1);
            }
        };
        $scope.bottom = function(){
            var cur = $scope.page;
            if(cur < $scope.numbers.length){
                $scope.pageMessage(cur+1);
            }
        };
        $scope.pageMessage = function(page){
            $scope.page = page;
            changeNumber(page);
            if(page == 1){
                $scope.left = false;
            }else{
                $scope.left = true;
            }
            if(page == $scope.numbers.length){
                $scope.right = false;
            }else{
                $scope.right = true;
            }
            $http.get("/api/logs?page=" + page).success(function(data){
                if(data.status == 1){
                    $scope.LogMember = data.data;
                }else {
                    return false
                }
            });
        };
        var pageNumbers = function(){
            $scope.Mlength = Math.ceil($scope.MemberLength / 10);
            for(var i = 1; i < $scope.Mlength+1; i++){
                $scope.numbers[i-1] = i;
            }
        };
        var init_length = function(){
            $scope.MemberLength = undefined;
            $http.get("/api/logs_length").success(function(data){
                if(data.status == 1){
                    $scope.MemberLength = data.data.length;
                    pageNumbers();
                }else{
                    console.log("some error");
                }
            });
        };
        init_length();
        var init = function(){
            $scope.pageMessage(1);
            $http.get("/api/logs?page=1").success(function(data){
                if(data.status == 1){
                    $scope.LogMember = data.data;
                }else{
                    console.log("some error");
                }
            });
        };
        init();
    });

