from rest_framework import serializers
from .models import Task, Tasklist, TaskTag
from django.contrib.auth.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    tasklists = serializers.StringRelatedField(many=True, read_only=True)
    password = serializers.CharField(write_only=True,
                                     style={'input_type': 'password'})

    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.username = validated_data['username']
        instance.set_password(validated_data['password'])
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ('username', 'password', 'tasklists')


class TasklistSharerSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=200)
    class Meta:
        fields = ('username', )


class TasklistSerializer(serializers.ModelSerializer):
    owner = serializers.CharField(max_length=200,
                                  source='user.username',
                                  read_only=True)
    tasks = serializers.StringRelatedField(many=True, read_only=True)
    sharers = TasklistSharerSerializer(many=True)
    lul = serializers.IntegerField

    class Meta:
        model = Tasklist
        fields = ('id', 'owner', 'name', 'sharers', 'tasks')
        read_only_fields = ('id', 'tasks')

    def create(self, validated_data):
        tasklist = Tasklist.objects.create(
            owner=validated_data['owner'],
            name=validated_data['name']
        )
        sharers = []
        for sharer in validated_data['sharers']:
            query = User.objects.filter(username=sharer['username'])
            if query:
                sharers.append(query[0])
        tasklist.sharers = sharers
        tasklist.save()
        return tasklist

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        input_sharers = validated_data.get('sharers', None)
        if input_sharers:
            sharers = []
            if input_sharers != [{}]:
                for sharer in input_sharers:
                    if sharer.get('username', None) != instance.owner.username:
                        query = User.objects.filter(username=sharer['username'])
                    else:
                        query = None
                    if query:
                        sharers.append(query[0])
            instance.sharers = sharers
        instance.save()
        return instance


class TaskTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskTag
        fields = ('name', )


class TaskSerializer(serializers.ModelSerializer):
    tags = TaskTagSerializer(many=True)

    class Meta:
        model = Task
        fields = ('id', 'name', 'description', 'completed',
                  'date_created', 'date_modified', 'due_date',
                  'priority', 'tags')
        read_only_fields = ('id', 'date_created', 'date_modified')

    def create(self, validated_data):
        task = Task.objects.create(
            name=validated_data['name'],
            description=validated_data['description'],
            completed=validated_data['completed'],
            due_date=validated_data['due_date'],
            priority=validated_data['priority'],
            tasklist_id=validated_data['tasklist'].id
        )
        tags = []
        for tag in validated_data['tags']:
            query = TaskTag.objects.filter(name=tag['name'])
            if query:
                tags.append(query[0])
            else:
                TaskTag.objects.create(name=tag['name'])
                tags.append(TaskTag.objects.get(name=tag['name']))
        task.tags = tags
        task.save()
        return task

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get(
            'description', instance.description)
        instance.completed = validated_data.get(
            'completed', instance.completed)
        instance.due_date = validated_data.get('due_date', instance.due_date)
        instance.priority = validated_data.get('priority', 'n')
        input_tags = validated_data.get('tags', None)
        if input_tags:
            tags = []
            if input_tags != [{}]:
                for tag in input_tags:
                    query = TaskTag.objects.filter(name=tag['name'])
                    if query:
                        tags.append(query[0])
                    else:
                        TaskTag.objects.create(name=tag['name'])
                        tags.append(TaskTag.objects.get(name=tag['name']))
            instance.tags = tags
        instance.save()
        return instance
