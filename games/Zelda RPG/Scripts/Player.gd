extends KinematicBody2D

const ACCELERATION = 50
const MAX_SPEED = 100
const FRICTION = 50

var velocity = Vector2.ZERO


func _physics_process(delta):
	var input_vector = Vector2.ZERO
	input_vector = get_player_input()
	velocity = calculate_velocity(input_vector, delta)
	move_and_collide(velocity)


func get_player_input():
	return Vector2(
		Input.get_action_strength("ui_right") - Input.get_action_strength("ui_left"),
		Input.get_action_strength("ui_down") - Input.get_action_strength("ui_up")
	).normalized()


func calculate_velocity(vector, delta):
	if vector != Vector2.ZERO:
		velocity += vector * ACCELERATION * delta
		velocity = velocity.clamped(MAX_SPEED * delta)
	else:
		velocity = velocity.move_toward(Vector2.ZERO, FRICTION * delta)
	return velocity
