extends KinematicBody2D

const ACCELERATION = 500
const MAX_SPEED = 80
const FRICTION = 500

var velocity = Vector2.ZERO

onready var animationPlayer = $AnimationPlayer
onready var animationTree = $AnimationTree
onready var animationState = animationTree.get("parameters/playback")


func _physics_process(delta):
	var input_vector = Vector2.ZERO
	input_vector = get_player_input()
	velocity = calculate_velocity(input_vector, delta)
	velocity = move_and_slide(velocity)


func get_player_input():
	return Vector2(
		Input.get_action_strength("ui_right") - Input.get_action_strength("ui_left"),
		Input.get_action_strength("ui_down") - Input.get_action_strength("ui_up")
	).normalized()
	

func calculate_velocity(vector, delta):
	if vector != Vector2.ZERO:
		animationTree.set("parameters/Idle/blend_position", vector)
		animationTree.set("parameters/Run/blend_position", vector)
		animationState.travel("Run")
		return velocity.move_toward(vector * MAX_SPEED, ACCELERATION * delta)
	else:
		animationState.travel("Idle")
		return velocity.move_toward(Vector2.ZERO, FRICTION * delta)
