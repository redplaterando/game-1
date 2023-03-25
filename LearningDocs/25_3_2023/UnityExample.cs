
public class GameObject
{
    List<Component> components;
}

public class Component
{
    void Update();
    void OnActivate();
    void OnDeactivate();
    void OnCollisionEnter();
    void OnCollisionExit();
    void OnMouseClicked();
}

public class PlayerComponent : Component
{
    void Update()
    {
        print("hello world");
        if(InputManager.IsKeyPressed(Key.W))
        {
            Jump();
        }
    }
}