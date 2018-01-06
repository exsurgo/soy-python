import com.google.inject.AbstractModule;
import com.google.template.soy.shared.restricted.SoyFunction;
import com.google.inject.multibindings.ProvidesIntoSet;
import com.google.inject.multibindings.Multibinder;

public class PluginsModule extends AbstractModule {

    public void configure() {

        Multibinder<SoyFunction> soyFunctionsSetBinder =
                Multibinder.newSetBinder(binder(), SoyFunction.class);

        // Bind all class functions here
        soyFunctionsSetBinder.addBinding().to(FooBarFunction.class);
        soyFunctionsSetBinder.addBinding().to(AddNumbersFunction.class);
        soyFunctionsSetBinder.addBinding().to(CallMethodFunction.class);

    }

    @ProvidesIntoSet
    public SoyFunction provideFooBar() {
        return new FooBarFunction();
    }

}