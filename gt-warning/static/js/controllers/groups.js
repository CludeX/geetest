angular.module('gtWarning')
    .controller('GroupCtrl', function ($scope,$rootScope,$http,$state){
        $scope.allGroups = [
            {_id: "group1", level: 1},
            {_id: "group2", level: 2},
            {_id: "group3", level: 3}
        ];
        $scope.newGroup = {
            _id: "",
            level:""
        };
        $scope.aGroup = {
            _id: "test",
            level: 10,
            members: []
        };
        $scope.allMember = [

        ];
        var MemberLength;
        $scope.showPop = false;
        $scope.showAdd = false;
        $scope.newGroupMessage = undefined;
        $scope.newMemberMessage = undefined;
        $scope.Member = [];
        $scope.setGroup = function (group) {
            $scope.Member = group.members;
            $scope.aGroup = group;
            console.log($scope.aGroup);
            $scope.showPop = true;
            MemberLength = $scope.Member.length;
            $scope.newMemberMessage = false;
            $scope.showAdd = false;
            console.log($scope.Member);
        };

        $scope.addGroupMember = function(){
            if(!$scope.showAdd){
                return $scope.showAdd = true;
            }else {
                return $scope.showAdd = false;
            }
        };
        var showAllMember = function(){
            $http.get("/api/members").success(function(data){
                if(data.status == 1){
                    $scope.allMember = data.data;
                }else{
                    console.log("some error");
                }
            });
        };
        showAllMember();

        $scope.addNewMeb = function($index){
            if($scope.Member.indexOf($scope.allMember[$index]._id)!= -1){
                return false;
            }else{
                $scope.Member.push($scope.allMember[$index]._id);
            }
        };

        $scope.AddNewSub = function(){
            var members = {
                _id: $scope.aGroup._id,
                members: $scope.Member
            };
            $http.post("/api/group_member",members).success(function(data){
                if(data.status == 1){
                    if(MemberLength == $scope.Member.length){
                        $scope.newMemberMessage = "";
                    }else {
                        $scope.newMemberMessage = "member 添加/删除成功";
                    }
                }else if(data.error) {
                    $scope.newGroupMessage = data.error;
                }else{
                    $scope.newGroupMessage = "添加失败";
                }
            });
        };


        $scope.delMember = function($index){
            var number = $index;
            $scope.Member.splice(number,1);
        };

        $scope.addGroup = function(group){
            $scope.newGroupMessage = false;
            if(!group._id){
                $scope.newGroupMessage = "请填写group name";
                return;
            } else if(!group.level){
                $scope.newGroupMessage = "请填写group level";
                return;
            }else{
                $http.post("/api/groups",group).success(function(data){
                    if (data.status == 1) {
                        $scope.newGroupMessage = "group 添加成功";
                        $scope.allGroups.push(group);
                    } else if (data.error) {
                        $scope.newGroupMessage = data.error;
                    } else {
                        $scope.newGroupMessage = "添加失败";
                    }
                });
            }
        };
        var init = function(){
            $http.get("/api/groups").success(function(data){
                if(data.status == 1){
                    $scope.allGroups = data.data;
                }else{
                    console.log("some error");
                }
            });
        };
        init();
    });





